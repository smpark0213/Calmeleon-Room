package kr.ac.gachon.tpsensor;

import android.database.Cursor;
import android.graphics.Color;
import android.os.AsyncTask;
import android.os.Bundle;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;

import com.google.android.gms.tasks.Task;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;
import com.prolificinteractive.materialcalendarview.CalendarDay;
import com.prolificinteractive.materialcalendarview.CalendarMode;
import com.prolificinteractive.materialcalendarview.MaterialCalendarView;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.concurrent.Executors;

public class Stats extends Fragment {

    private final OneDayDecorator oneDayDecorator = new OneDayDecorator();
    MaterialCalendarView materialCalendarView;
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
    }

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View v=inflater.inflate(R.layout.stats,container,false);
        FirebaseDatabase database = FirebaseDatabase.getInstance();
        DatabaseReference dateRef = database.getReference("Decorate");
        ArrayList<Object> value = new ArrayList<>();
        ArrayList<String> valueDate = new ArrayList<>();
        ArrayList<String> valueColor = new ArrayList<>();

        dateRef.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot dataSnapshot) {
                for (DataSnapshot snapshot : dataSnapshot.getChildren())
                {
                    Object date = snapshot.getValue(Object.class);
                    value.add(date);
                }

                for (int i = 0; i < value.size(); i++)
                {
                    String temp = value.get(i).toString();
                    String[] temp1 = temp.split("date=");
                    String[] date = temp1[1].split(",");
                    String[] temp2 = temp1[1].split("color=");
                    String[] color = temp2[1].split("\\}");
                    valueDate.add(date[0]);
                    valueColor.add(color[0]);
                }

                for (int i = 0; i < value.size(); i++)
                {
                    String date = valueDate.get(i);
                    int year = Integer.parseInt(date.substring(0, 4));
                    int month = Integer.parseInt(date.substring(4, 6));
                    int day = Integer.parseInt(date.substring(6, 8));
                    String color = valueColor.get(i);
                    if (color.equalsIgnoreCase("blue"))
                    {
                        materialCalendarView.addDecorator( new EventDecorator(Color.BLUE, Collections.singleton(CalendarDay.from(year, month - 1, day))));
                    }
                    if (color.equalsIgnoreCase("yellow"))
                    {
                        materialCalendarView.addDecorator( new EventDecorator(Color.YELLOW, Collections.singleton(CalendarDay.from(year, month - 1, day))));
                    }
                    if (color.equalsIgnoreCase("pink"))
                    {
                        materialCalendarView.addDecorator( new EventDecorator(Color.rgb(255, 228, 225), Collections.singleton(CalendarDay.from(year, month - 1, day))));
                    }
                    if (color.equalsIgnoreCase("red"))
                    {
                        materialCalendarView.addDecorator( new EventDecorator(Color.RED, Collections.singleton(CalendarDay.from(year, month - 1, day))));
                    }
                    if (color.equalsIgnoreCase("green"))
                    {
                        materialCalendarView.addDecorator( new EventDecorator(Color.GREEN, Collections.singleton(CalendarDay.from(year, month - 1, day))));
                    }
                }
            }

            @Override
            public void onCancelled(@NonNull DatabaseError error) {

            }
        });

        materialCalendarView = (MaterialCalendarView)v.findViewById(R.id.calendarView);
        materialCalendarView.state().edit()
                .setFirstDayOfWeek(Calendar.SUNDAY)
                .setMinimumDate(CalendarDay.from(2021, 0, 1))
                .setMaximumDate(CalendarDay.from(2030, 11, 31))
                .setCalendarDisplayMode(CalendarMode.MONTHS)
                .commit();
        materialCalendarView.addDecorators(
                new SundayDecorator(),
                new SaturdayDecorator(),
                oneDayDecorator);



        return v;
    }
}
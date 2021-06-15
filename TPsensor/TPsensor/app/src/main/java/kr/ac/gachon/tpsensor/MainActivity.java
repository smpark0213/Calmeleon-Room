package kr.ac.gachon.tpsensor;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;

import android.Manifest;
import android.os.Build;
import android.os.Bundle;
import android.view.MenuItem;

import com.google.android.material.bottomnavigation.BottomNavigationView;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;

public class MainActivity extends AppCompatActivity {
    private static final String TAG = "Main_Activity";

    private BottomNavigationView mBottomNavigationView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        ActivityCompat.requestPermissions(this, new String[]{Manifest.permission.RECORD_AUDIO}, 1);
        setContentView(R.layout.activity_main);

        mBottomNavigationView=findViewById(R.id.bottom_navigation);

        getSupportFragmentManager().beginTransaction().add(R.id.frame_container,new Record()).commit();

        mBottomNavigationView.setOnNavigationItemSelectedListener(new BottomNavigationView.OnNavigationItemSelectedListener() {
            @Override
            public boolean onNavigationItemSelected(@NonNull MenuItem item) {
                switch (item.getItemId()){
                    case R.id.nav_record :
                        getSupportFragmentManager().beginTransaction().replace(R.id.frame_container,new Record()).commit();
                        break;
                    case R.id.nav_stats:
                        getSupportFragmentManager().beginTransaction().replace(R.id.frame_container,new Stats()).commit();
                        break;
                }
                return true;
            }
        });
    }
}
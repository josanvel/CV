package com.prototiposs;

import android.os.Bundle;
import android.app.Activity;
import android.content.Intent;
import android.view.*;
import android.view.View.OnClickListener;

public class MenuP extends Activity implements OnClickListener{
	@Override
	public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity2);
        View btn1 = findViewById(R.id.button1);
        btn1.setOnClickListener(this);
        View btn2 = findViewById(R.id.button2);
        btn2.setOnClickListener(this);
        View btn3 = findViewById(R.id.button3);
        btn3.setOnClickListener(this);
        View btn4 = findViewById(R.id.button4);
        btn4.setOnClickListener(this);
    }
    
    public void onClick(View vista){
    	if(vista.getId() == findViewById(R.id.button1).getId()){
    		Intent intento = new Intent(this, NewNote.class );
    		startActivity(intento);
    	}
    	else if(vista.getId() == findViewById(R.id.button2).getId()){
    		Intent intento = new Intent(this, ViewNote.class);
    		startActivity(intento);
    	}
    	else if(vista.getId() == findViewById(R.id.button3).getId()){
    		Intent intento = new Intent(this, PagesSave.class);
    		startActivity(intento);
    	}
    	else if(vista.getId() == findViewById(R.id.button4).getId()){
    		finish();

    	}
    }

}

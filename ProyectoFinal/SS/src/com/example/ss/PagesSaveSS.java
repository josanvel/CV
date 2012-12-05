package com.example.ss;

import android.app.Activity;
import android.os.Bundle;
import android.view.View;

public class PagesSaveSS extends Activity {

	@Override
	public void onCreate(Bundle saveInstanceState){
		super.onCreate(saveInstanceState);
		setContentView(R.layout.page_save_activity);
	}

	public void onClick(View vista){
		switch(vista.getId()){
			case R.id.B_BackPS:{
				finish();
			}
		}
	}
}

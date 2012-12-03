package com.example.ss;

import android.os.Bundle;
import android.os.Handler;
import android.os.Message;
import android.app.Activity;
import android.content.Intent;
import android.widget.SeekBar;

public class MenuActivity extends Activity {

	SeekBar sb;
	Intent inten;
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.loading_activity);
        sb = (SeekBar)findViewById(R.id.seekBar1);
    }

	Handler handler = new Handler(){
		@Override
		public void handleMessage(Message msg){
			sb.incrementProgressBy(5);
		}
	};
    boolean isRunning = false;
	
	public void onStart(){
		super.onStart();
		sb.setProgress(0);
		
		Thread th = new Thread(new Runnable() {
			public void run() {
				try{
					for(int i=0; i<20 && isRunning; i++){
						Thread.sleep(200);
						handler.sendMessage(handler.obtainMessage());
					}
					inicio();
				}catch(Throwable e){}
			}
		});
		isRunning = true;
		th.start();
	}
	
	public void onStop(){
		super.onStop();
		isRunning = false;
	}
	
	public void inicio(){
		inten = new Intent(this, MainPrincipal.class);
		finish();
		startActivity(inten);
	}
}

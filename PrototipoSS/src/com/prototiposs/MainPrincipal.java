package com.prototiposs;

import android.os.Bundle;
import android.os.Handler;
import android.os.Message;
import android.app.Activity;
import android.content.Intent;
import android.widget.SeekBar;

public class MainPrincipal extends Activity {
	SeekBar sb;
	Intent inten;
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity1);
        sb = (SeekBar)findViewById(R.id.seekBar1);
    }

	Handler handler = new Handler()
	{
		@Override
		public void handleMessage(Message msg)
		{
			sb.incrementProgressBy(5);
		}
	};
    boolean isRunning = false;
	
	public void onStart()
	{
		super.onStart();
		sb.setProgress(0);
		
		Thread th = new Thread(new Runnable() {
			public void run() {
				// TODO Auto-generated method stub
				try{
					for(int i=0; i<20 && isRunning; i++)
					{
						Thread.sleep(200);
						handler.sendMessage(handler.obtainMessage());
					}
					inicio();
				}catch(Throwable e)
				{}
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
		inten = new Intent(this, MenuP.class);
		startActivity(inten);
	}
}

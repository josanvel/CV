package com.example.ss;

import android.os.Bundle;
import android.app.Activity;
import android.content.Intent;
import android.view.View;

public class MainPrincipal extends Activity {

	@Override
	public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_principal_main);
    }
    
    public void onClick(View vista){
    	
    	switch(vista.getId()){
    		case R.id.B_NewNote:{
    			Intent intento = new Intent(this, NewNoteSS.class );
        		startActivity(intento);
    		}break;
    		
    		case R.id.B_ViewNote:{
        		Intent intento = new Intent(this, ViewNoteSS.class);
        		startActivity(intento);
    		}break;
    		
    		//case R.id.B_PageSave:{
        		//Intent intento = new Intent(this, PagesSaveSS.class);
        		//startActivity(intento);
    		//}break;
    		
    		case R.id.B_Exit:{
    			 setResult(RESULT_OK);
        		 finish();
    		}break;
    	}
    }
}

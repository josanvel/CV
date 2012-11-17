package com.prototiposs;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.view.View.OnClickListener;

public class PagesSave extends Activity implements OnClickListener {

	@Override
	public void onCreate(Bundle saveInstanceState){
		super.onCreate(saveInstanceState);
		setContentView(R.layout.activity5);
		
		View boton1 = findViewById(R.id.B_A);
		boton1.setOnClickListener(this);
		//View boton2 = findViewById(R.id.B_aceptar);
		//boton2.setOnClickListener(this);
	}

	public void onClick(View vista){
		if(vista.getId() == findViewById(R.id.B_A).getId()){
			Intent intento1 = new Intent(this,MenuP.class);
			startActivity(intento1);
		}
	}
}

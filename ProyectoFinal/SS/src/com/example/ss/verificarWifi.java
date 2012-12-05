package com.example.ss;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;

import com.pdfcrowd.Client;
import com.pdfcrowd.PdfcrowdError;

import BD.DBAdapter;
import android.app.ListActivity;
import android.app.Service;
import android.content.Context;
import android.content.Intent;
import android.database.Cursor;
import android.net.wifi.WifiManager;
import android.os.Environment;
import android.os.IBinder;
import android.widget.SimpleCursorAdapter;
import android.widget.Toast;

public class verificarWifi extends ListActivity implements Runnable{
	private String page,data,urlComplet,nota;
	private DBAdapter dbHelper;
	private Cursor cursor;

	public void run() {
		WifiManager wifiManager = (WifiManager) getSystemService(Context.WIFI_SERVICE);
		try {
			wifiManager.setWifiEnabled(true);
		} catch (Exception e) {
			Toast toast = Toast.makeText(getApplicationContext(),"Error al activar WiFi", Toast.LENGTH_LONG);
			toast.show();
		}
		
		dbHelper = new DBAdapter(this);
		dbHelper.open();
		fillData();
	}

	@Override
	public String toString(){
	   	page = data+""+nota;
		return page;
	}
	
	public void searchPage(String nota, String categoria, String buscador){
		generatePDF(nota, categoria,buscador);
   }
	
   public void generatePDF(String name, String categoria, String buscador){ 
	   	   
		   File f =null ,directoryAcademico,sdCard,directoryCulturaGeneral;
		   
		   sdCard = Environment.getExternalStorageDirectory();
		   if(buscador.equalsIgnoreCase("wikipedia"))
			   data = "http://es.wikipedia.org/wiki/";
		   else if(buscador.equalsIgnoreCase("diccionario"))
			   data = "http://www.wordreference.com/definicion/";
		   
		   urlComplet = toString();
		   
		   try {
			   directoryAcademico = new File(sdCard.getAbsolutePath()+ "/PDF-ACADEMICO");
			   directoryAcademico.mkdirs();
			   
			   directoryCulturaGeneral = new File(sdCard.getAbsolutePath()+ "/PDF-CULTURA-GENERAL");
			   directoryCulturaGeneral.mkdirs();
				   
			   if(categoria.equalsIgnoreCase("academico"))
					   f = new File(directoryAcademico, name+".pdf");
				   else
					   f = new File(directoryCulturaGeneral, name+".pdf"); 
			   if(!f.exists()){
				   try{
			            FileOutputStream fileStream; 
			            Client client = new Client("josanvel", "227401e8727914dbe745f8ab36a6cab2");
			            fileStream = new FileOutputStream(f);
			            client.convertURI(urlComplet,fileStream );
			            fileStream.close();
			        }
			        catch(PdfcrowdError why) { }
			        catch(IOException exc) {}
			   }else{ 
			   Toast.makeText(getBaseContext(), "File already Exist", Toast.LENGTH_LONG).show(); 
			   } 
		   }catch (Exception e){ 
			   Toast.makeText(getBaseContext(), "Error Occured", Toast.LENGTH_LONG).show();
		   }
	}
   private void fillData() {
		cursor = dbHelper.fetchAllTodos();
		startManagingCursor(cursor);

		String[] from = new String[] { DBAdapter.KEY_SUMMARY };
		int[] to = new int[] { R.id.label };

		//Creamos un array adapter para desplegar cada una de las filas
		SimpleCursorAdapter notes = new SimpleCursorAdapter(this, R.layout.row, cursor, from, to);
		notes.toString();
		
		//setListAdapter(notes);
	}

}

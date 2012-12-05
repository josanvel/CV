package com.example.ss;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import com.itextpdf.text.pdf.PdfWriter;
import com.pdfcrowd.Client;
import com.pdfcrowd.PdfcrowdError;

import BD.DBAdapter;
import android.app.Activity;
import android.content.Context;
import android.database.Cursor;
import android.net.wifi.WifiManager;
import android.os.Bundle;
import android.os.Environment;
import android.util.Log;
import android.view.View;
import android.widget.EditText;
import android.widget.Spinner;
import android.widget.TextView;
import android.widget.Toast;

public class NewNoteSS extends Activity{
	
	private String page;
	PdfWriter writer, w;
	private EditText texNewNote=null;
	private EditText textID=null;
	private Long mRowId=null;
	private DBAdapter mDbHelper=null;
	private Spinner mCategory;
	private Spinner mSearcher;
	private String nota, cate, search;
	String strHtml, pdfhtml;
	String data,urlComplet;
	@Override
	public void onCreate(Bundle bundle){
		super.onCreate(bundle);
		
		mDbHelper = new DBAdapter(this);
		mDbHelper.open();
		
		setContentView(R.layout.newnote);
		mCategory = (Spinner) findViewById(R.id.category);
		mSearcher = (Spinner) findViewById(R.id.searcher);
		texNewNote=(EditText)findViewById(R.id.txt_Note);
		textID = (EditText) findViewById(R.id.txt_Note);

		mRowId = null;
		Bundle extras = getIntent().getExtras();
		mRowId = (bundle == null) ? null : (Long) bundle.getSerializable(DBAdapter.KEY_ROWID);
		if(extras != null){
			mRowId = extras.getLong(DBAdapter.KEY_ROWID);
		}	
		populateFields();
	}
	
	public void onClick(View vista){
		WifiManager wifiManager = (WifiManager) getSystemService(Context.WIFI_SERVICE);
    	switch(vista.getId()){
    		case R.id.B_BackNN:{
    			setResult(RESULT_OK);
				finish();
    		}break;
    		
    		case R.id.B_SaveNN:{
    			TextView resultado = (TextView)findViewById(R.id.lb_MensajeNewNote);
				cate = mCategory.getSelectedItem().toString();
				search = mSearcher.getSelectedItem().toString();
				nota = texNewNote.getText().toString();
				resultado.setText("Frase "+nota.toUpperCase() +" Guardarda \n Categoria : "+cate+"\nBusacdor : "+search);
				try {
					wifiManager.setWifiEnabled(true);
				} catch (Exception e) {
					Toast toast = Toast.makeText(getApplicationContext(),"Error al activar WiFi", Toast.LENGTH_LONG);
					toast.show();
				}
				
				new Thread(new Runnable() {
				    public void run() {
				    	runOnUiThread(new Runnable() {
				            public void run() {
						    	searchPage(nota,cate,search);
				            }
				        });
				    }
				}).start();

    		}break;
    	}
    }
	
	
	private void populateFields() {
		if (mRowId != null) {
			Cursor todo = mDbHelper.fetchTodo(mRowId);
			startManagingCursor(todo);
			String category = todo.getString(todo.getColumnIndexOrThrow(DBAdapter.KEY_CATEGORY));
			for (int i=0; i<mCategory.getCount();i++){
							
				String s = (String) mCategory.getItemAtPosition(i); 
				Log.e(null, s +" " + category);
				if (s.equalsIgnoreCase(category)){
						mCategory.setSelection(i);
				}
			}
			texNewNote.setText(todo.getString(todo.getColumnIndexOrThrow(DBAdapter.KEY_SUMMARY)));
			textID.setText(todo.getString(todo.getColumnIndexOrThrow(DBAdapter.KEY_DESCRIPTION)));
		}
	}
	
	protected void onSaveInstanceState(Bundle outState) {
		super.onSaveInstanceState(outState);
		saveState();
		outState.putSerializable(DBAdapter.KEY_ROWID, mRowId);
	}
	
    @Override
    protected void onPause() {
      super.onPause();
      saveState();
    }
    
    @Override
    protected void onResume() {
		super.onResume();
		populateFields();
    }
    
   private void saveState() {
    	String category = (String) mCategory.getSelectedItem();
    	String seacher = (String) mSearcher.getSelectedItem();
		String summary = texNewNote.getText().toString();
		String description = texNewNote.getText().toString();
		
		if (mRowId == null) {
			long id = mDbHelper.createTodo(category, summary, description);
			if (id > 0) 
				mRowId = id;
		}else
			mDbHelper.updateTodo(mRowId, category, summary, description);
    }
   //Spbreescribo el metodo ToString
   
   @Override
	public String toString(){
	   	page = data+""+nota;
		return page;
	}
   
 //Obtengo el codigo HTML
   public void searchPage(String nota, String categoria, String buscador){
		//Toast.makeText(NewNoteSS.this, strHtml, Toast.LENGTH_LONG).show(); 
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
			   try 
		        {
		            FileOutputStream fileStream; 
		            // create an API client instance
		            Client client = new Client("josanvel", "227401e8727914dbe745f8ab36a6cab2");
		            // convert a web page and save the PDF to a file
		            //fileStream = new FileOutputStream("example.pdf");
		            fileStream = new FileOutputStream(f);
		            Toast.makeText(NewNoteSS.this,"pasa", Toast.LENGTH_LONG).show();
		            Toast.makeText(NewNoteSS.this, urlComplet, Toast.LENGTH_LONG).show();
		            client.convertURI(urlComplet,fileStream );
		            fileStream.close();
		            Toast.makeText(NewNoteSS.this,"se creo pdf", Toast.LENGTH_LONG).show();
		        }
		        catch(PdfcrowdError why) {
		        	Toast.makeText(NewNoteSS.this,"error al crear pdf", Toast.LENGTH_LONG).show();
		        }
		        catch(IOException exc) {}
		
		   }else{ 
		   Toast.makeText(getBaseContext(), "File already Exist", Toast.LENGTH_LONG).show(); 
		   } 
	   }catch (Exception e){ 
		   Toast.makeText(getBaseContext(), "Error Occured", Toast.LENGTH_LONG).show();
	   }
   	}  
   	
   	
}

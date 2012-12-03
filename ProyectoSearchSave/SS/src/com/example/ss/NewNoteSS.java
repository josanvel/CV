package com.example.ss;

import java.io.File;
import java.io.FileOutputStream;
import java.io.StringReader;

import pdftron.PDF.HTML2PDF;
import pdftron.PDF.PDFDoc;
import pdftron.PDF.PDFNet;

import com.itextpdf.text.PageSize;
import com.itextpdf.text.html.simpleparser.HTMLWorker;
import com.itextpdf.text.pdf.PdfWriter;

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
import BD.*;

public class NewNoteSS extends Activity{
	private String data = "http://es.wikipedia.org/";
	private String page;
	PdfWriter writer, w;
	private EditText texNewNote=null;
	private EditText textID=null;
	private Long mRowId=null;
	private DBAdapter mDbHelper=null;
	private Spinner mCategory;
	private String nota, cate;
	String strHtml, pdfhtml;
	private ObtenerHtml strHTML = new ObtenerHtml();
	private ConvertirPDF pdfHTML = new ConvertirPDF();
	//final private WifiManager wifiManager = (WifiManager) getSystemService(Context.WIFI_SERVICE);
	
	@Override
	public void onCreate(Bundle bundle){
		super.onCreate(bundle);
		
		mDbHelper = new DBAdapter(this);
		mDbHelper.open();
		
		setContentView(R.layout.newnote);
		mCategory = (Spinner) findViewById(R.id.category);
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
				nota = texNewNote.getText().toString();
				resultado.setText("Frase "+nota.toUpperCase() +" Guardarda \n Categoria : "+cate);
				//texNewNote.setText("");
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
						    	searchPage(nota,cate);
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
   public void searchPage(String nota, String categoria){
		strHtml = strHTML.getHtml(toString());
		//Toast.makeText(NewNoteSS.this, strHtml, Toast.LENGTH_LONG).show(); 
		pdfhtml = generatePDF(strHtml, nota, categoria);
   }
   
   
   
   	public String generatePDF(String htmls ,String name, String categoria){ 
   		//PDFNet.initialize();
	   String path = null ;
	   File f =null ,directoryAcademico,sdCard,directoryCulturaGeneral;
	   
	   sdCard = Environment.getExternalStorageDirectory();
	   try {
		   //HTML2PDF.setModulePath("../../../Lib/");
		   //PDFDoc doc = new PDFDoc();
		  // HTML2PDF converter = new HTML2PDF();
		   //converter.insertFromHtmlString(htmls);
		   
		   
		   directoryAcademico = new File(sdCard.getAbsolutePath()+ "/PDF-ACADEMICO");
		   directoryAcademico.mkdirs();
		   
		   directoryCulturaGeneral = new File(sdCard.getAbsolutePath()+ "/PDF-CULTURA-GENERAL");
		   directoryCulturaGeneral.mkdirs();
		   
		  // if ( converter.convert(doc) ){
			   
			   if(categoria.equalsIgnoreCase("academico"))
				   f = new File(directoryAcademico, name+".pdf");
			   else
				   f = new File(directoryCulturaGeneral, name+".pdf");
		   //}
		   
		   Log.v("genratePDF", "new file"); 
		   //f.delete();
		   if(!f.exists()){
			   
			   path = f.getPath(); 
			   //Toast.makeText(getBaseContext(), path, Toast.LENGTH_LONG).show(); 
		
			   StringBuffer buf = new StringBuffer(" <table width='1000' height='10000' border='1' bordercolor=\"1\" cellspacing='0' cellpadding='1'>"); 
		    	buf.append("<tr><td height='100' bgcolor=\"#D8D8D8\"> jose y karen\n daniel y liliana </td></tr></table>"); 

			   String htstr=buf.toString(); 
		
			   com.itextpdf.text.Document document = new com.itextpdf.text.Document(PageSize.A4,38,38,50,30); 
			   PdfWriter w= PdfWriter.getInstance(document, new FileOutputStream(path));
		
			   document.open(); 
		
			   HTMLWorker htmlWorker = new HTMLWorker(document); 
			   htmlWorker.parse(new StringReader(htstr)); 
			   document.close(); 
		
		   }else{ 
		   Toast.makeText(getBaseContext(), "File already Exist", Toast.LENGTH_LONG).show(); 
		   } 
	   }catch (Exception e){ 
		   Toast.makeText(getBaseContext(), "Error Occured", Toast.LENGTH_LONG).show();
	   }
	   //PDFNet.terminate();
	   return path;
   	}   
}

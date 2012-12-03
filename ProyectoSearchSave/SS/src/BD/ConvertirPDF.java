package BD;

import java.io.*;

import pdftron.PDF.HTML2PDF;
import pdftron.PDF.PDFDoc;
import pdftron.PDF.PDFNet;

import com.itextpdf.text.PageSize;
import com.itextpdf.text.html.simpleparser.HTMLWorker;
import com.itextpdf.text.pdf.PdfWriter;
import android.app.Activity;
import android.os.Environment;
import android.util.Log;
import android.widget.Toast;

public class ConvertirPDF extends Activity{
	PdfWriter writer, w;
	public ConvertirPDF(){}
	
	String output_path = "../../TestFiles/Output/html2pdf_example";

	// The first step in every application using PDFNet is to initialize the 
	// library and set the path to common PDF resources. The library is usually 
	// initialized only once, but calling Initialize() multiple times is also fine.
//PDFNet.initialize();

	// For HTML2PDF we need to locate the html2pdf module. If placed with the 
	// PDFNet library, or in the current working directory, it will be loaded
	// automatically. Otherwise, it must be set manually using HTML2PDF.SetModulePath.


public void /*PDFdoc*/ ConvertirPdf(String html, String NamePage){
PDFNet.initialize();
 File ruta_sd = null;
 File sdCard, directory, file = null;
	String str="";
	// Clase que permite grabar texto en un archivo
    sdCard = Environment.getExternalStorageDirectory();
	FileOutputStream fout = null;
	
try 
{
    HTML2PDF.setModulePath("../../../Lib/");
    
    PDFDoc doc = new PDFDoc();
	HTML2PDF converter = new HTML2PDF();
			// Our HTML data
			// Add html data
	converter.insertFromHtmlString(html);
			// Note, InsertFromHtmlString can be mixed with the other Insert methods.
	
	if ( converter.convert(doc) ){				
		try{
			// instanciamos un onjeto File para crear un nuevo
			// directorio
			// la memoria externa
			directory = new File(sdCard.getAbsolutePath()+ "/Mis archivos");
			// se crea el nuevo directorio donde se cerara el
			// archivo
			directory.mkdirs();
			// creamos el archivo en el nuevo directorio creado
			file = new File(directory, NamePage+".pdf");
		}catch(Exception e){/*Toast.makeText(n, "Error de try-catch", Toast.LENGTH_LONG).show();*/}
	}		    
}
catch (Exception e){
	e.printStackTrace();
    return;
}
PDFNet.initialize();
//return doc;
}
	
	
	
	
	public String generatePDF(String t){ 
   	 String path = null ; 
   	 try { 

   	 File f = new File(Environment.getExternalStorageDirectory(), "emiliano.pdf"); 
   	 Log.v("genratePDF", "new file"); 
	    	 if(f.exists()) 
	    	 { 
		    	 path = f.getPath(); 
		    	 Toast.makeText(getBaseContext(), path, Toast.LENGTH_LONG).show(); 
		    	 StringBuffer buf = new StringBuffer(" <table width='10000' border='1' bordercolor=\"1\" cellspacing='0' cellpadding='100'>");
		    	 buf.append("<tr><td height='30' bgcolor=\"#D8D8D8\"> Hello this is test message</td></tr></table>");
		    	 //buf.append(t); 
		
		    	 String htstr=buf.toString(); 
		    	 com.itextpdf.text.Document document = new com.itextpdf.text.Document(PageSize.A4); 
		    	 writer = PdfWriter.getInstance(document, new FileOutputStream(path)); 
		    	 w= PdfWriter.getInstance(document, new FileOutputStream(path));
		
		    	 document.open(); 
		
		    	 HTMLWorker htmlWorker = new HTMLWorker(document); 
		    	 htmlWorker.parse(new StringReader(htstr)); 
		    	 document.close(); 
		
	    	 }else
	    		 Toast.makeText(getBaseContext(), "File already Exist", Toast.LENGTH_LONG).show(); 
   	 } 
   	 catch (Exception e) { 
   		 Toast.makeText(getBaseContext(), "Error Occured", Toast.LENGTH_LONG).show();
   	 }
   	 return path;
   }

}

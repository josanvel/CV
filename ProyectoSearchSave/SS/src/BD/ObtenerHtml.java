package BD;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

import org.apache.http.HttpResponse;
import org.apache.http.NameValuePair;
import org.apache.http.client.HttpClient;
import org.apache.http.client.entity.UrlEncodedFormEntity;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.message.BasicNameValuePair;

public class ObtenerHtml {
	String html;
	
	public ObtenerHtml(){}
	
	public String getHtml(String Strhtml){
		String StringHtml = null;
		BufferedReader in = null;
		
		try {
			HttpClient client = new DefaultHttpClient();
			HttpPost request = new HttpPost(Strhtml);
	
			List<NameValuePair> postParameters = new ArrayList<NameValuePair>();
			postParameters.add(new BasicNameValuePair("one", "valueGoesHere"));
	
			UrlEncodedFormEntity formEntity = new UrlEncodedFormEntity(postParameters);
			request.setEntity(formEntity);
	
			HttpResponse response = client.execute(request);
			in = new BufferedReader(new InputStreamReader(response.getEntity().getContent()));
	
			StringBuffer sb = new StringBuffer("");
			String line = "";
			String NL = System.getProperty("line.separator");
	
			while ((line = in.readLine()) != null) {
			sb.append(line + NL);
			}
			in.close();
			StringHtml = sb.toString();
			
			if (in != null) {
					in.close();
			}
		} catch (Exception e){	}
		
		return StringHtml;
	}

}

package com.example.ss;
import BD.DBAdapter;
import android.app.ListActivity;
import android.content.Intent;
import android.database.Cursor;
import android.os.Bundle;
import android.view.ContextMenu;
import android.view.ContextMenu.ContextMenuInfo;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.AdapterView.AdapterContextMenuInfo;
import android.widget.ListView;
import android.widget.SimpleCursorAdapter;
import android.widget.Toast;

public class ViewNoteSS extends ListActivity {
	
	private DBAdapter dbHelper;
	private static final int ACTIVITY_CREATE = 0;
	private static final int ACTIVITY_EDIT = 1;
	private static final int DELETE_ID = Menu.FIRST + 1;
	private Cursor cursor;
    /** Called when the activity is first created. */
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.view_note_activity);
        
        
        this.getListView().setDividerHeight(2);
		dbHelper = new DBAdapter(this);
		dbHelper.open();
		fillData();
		registerForContextMenu(getListView());
    }
    
    public void onClick(View vista){
    	switch(vista.getId()){
    	   case R.id.B_BackVN:{
    		   setResult(RESULT_OK);
    		   finish();
    		}break;
    	}
    }
    
   	@Override
 	public boolean onContextItemSelected(MenuItem item) {
 		switch (item.getItemId()) {
 		case DELETE_ID:
 			AdapterContextMenuInfo info = (AdapterContextMenuInfo) item.getMenuInfo();
 			dbHelper.deleteTodo(info.id);
 			fillData();
 			return true;
 		}
 		return super.onContextItemSelected(item);
 	}
 	//ListView y la accion al seleccionar un item
 	@Override
 	protected void onListItemClick(ListView l, View v, int position, long id) {
 		
 		super.onListItemClick(l, v, position, id);
 		Intent i = new Intent(this, NewNoteSS.class);
 		i.putExtra(DBAdapter.KEY_ROWID, id);
 		startActivityForResult(i, ACTIVITY_EDIT);
 	}
 	@Override
 	protected void onActivityResult(int requestCode, int resultCode, Intent intent) {
 		super.onActivityResult(requestCode, resultCode, intent);
 		fillData();
 	}

 	//@SuppressWarnings("deprecation")
	private void fillData() {
 		cursor = dbHelper.fetchAllTodos();
 		startManagingCursor(cursor);

 		String[] from = new String[] { DBAdapter.KEY_SUMMARY };
 		int[] to = new int[] { R.id.label };

 		//Creamos un array adapter para desplegar cada una de las filas
		SimpleCursorAdapter notes = new SimpleCursorAdapter(this, R.layout.row, cursor, from, to);
		//notes.;
		Toast.makeText(ViewNoteSS.this, notes.toString(), Toast.LENGTH_LONG).show();
 		setListAdapter(notes);
 	}

 	@Override
 	public void onCreateContextMenu(ContextMenu menu, View v, ContextMenuInfo menuInfo) {
 		super.onCreateContextMenu(menu, v, menuInfo);
 		menu.add(0, DELETE_ID, 0, R.string.deleteNewNote);
 		menu.add(0, 4, 0, R.string.cancelNewNote);
 	}
 	
 	@Override
 	protected void onDestroy() {
 		super.onDestroy();
 		if (dbHelper != null) {
 			dbHelper.close();
 		}
 	}
}
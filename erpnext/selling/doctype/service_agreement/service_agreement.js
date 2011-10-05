//Make Invoice
cur_frm.cscript['Make Invoice'] = function(doc,cdt,cdn) {
  cur_frm.cscript.make_inv();
  }
cur_frm.cscript['Service Visit'] = function(doc,cdt,cdn) {
  cur_frm.cscript.service_visit();
}

cur_frm.cscript.make_inv = function() {
//	var sa_detail = LocalDB.getchildren('SA Detail',doc.name,'items','Service Agreement');
  var rv = LocalDB.create('Receivable Voucher');
  rv = locals['Receivable Voucher'][rv];
  rv.posting_date = doc.date;
  rv.due_date = doc.date;
  rv.voucher_date = doc.date;
  rv.customer = doc.customer;
//  rv.fiscal_year = doc.fiscal_year;
//  rv.company = doc.company;
  
  loaddoc('Receivable Voucher', rv.name);
}

cur_frm.cscript.service_visit = function(doc,dt,dn){
	var d = new wn.widgets.Dialog({
		width: 500,
		title: 'Service Visit',
		fields: [
			{fieldtype:'Data', label:'Serial Number', fieldname:'serial_number', reqd:1},
			{fieldtype:'Date', label:'Visit Date', fieldname:'visit_date', reqd:1},
			{fieldtype:'Text', label:'Visit Details', fieldname:'visit_details', reqd:1},
			{fieldtype:'Button', label:'Update',fieldname:'update'}
		]
	})
	d.show();
	d.fields_dict.update.input.onclick = function(doc,dt,dn) {
		var data = d.get_values();

		if(data) {
			$c_obj(make_doclist(dt,dn),'service_visit_post',data,function(){cur_frm.refresh(); d.hide();});
		}
	}
}

cur_frm.cscript.refresh = function(doc)
{
	if(doc.docstatus==0) {
		hide_field('Make Invoice');
		hide_field('Service Visit');
	} else if (doc.docstatus==1) {
		unhide_field('Make Invoice');
		unhide_field('Service Visit');
	}
}


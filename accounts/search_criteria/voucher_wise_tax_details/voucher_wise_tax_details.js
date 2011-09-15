report.customize_filters = function() {
  this.hide_all_filters();

  //Add filter
  this.add_filter({fieldname:'based_on', label:'Based On', fieldtype:'Select', options:'Sales Order'+NEWLINE+'Delivery Note'+NEWLINE+'Sales Invoice', report_default:'Sales Invoice', ignore : 1,parent:'RV Tax Detail', single_select :1, in_first_page:1});
  
  this.add_filter({fieldname:'posting_date', label:'Date', fieldtype:'Date', options:'', ignore : 1,parent:'RV Tax Detail', in_first_page:1});
  
  this.add_filter({fieldname:'voucher_id', label:'Voucher Id', fieldtype:'Data', options:'', ignore : 1,parent:'RV Tax Detail', in_first_page:1});
  
  this.add_filter({fieldname:'tax_account', label:'Tax Account', fieldtype:'Link', options:'Account', ignore : 1,parent:'RV Tax Detail', in_first_page:1});
}


// hide sections
//--------------------------------------
this.mytabs.items['More Filters'].hide();
this.mytabs.items['Select Columns'].hide();

// Get query
//--------------------------------------
report.get_query = function() {
  based_on = this.get_filter('RV Tax Detail', 'Based On').get_value();
  from_date = this.get_filter('RV Tax Detail', 'From Date').get_value();
  to_date = this.get_filter('RV Tax Detail', 'To Date').get_value();
  vid = this.get_filter('RV Tax Detail', 'Voucher Id').get_value();
  acc = this.get_filter('RV Tax Detail', 'Tax Account').get_value();

  date_fld = 'transaction_date';
  if(based_on == 'Sales Invoice') {
  	based_on = 'Receivable Voucher';
  	date_fld = 'voucher_date';
  }

  sp_cond = '';
  if (from_date) sp_cond += repl(' AND t1.%(dt)s >= "%(from_date)s"', {dt:date_fld, from_date:from_date});
  if (to_date) sp_cond += repl(' AND t1.%(dt)s <= "%(to_date)s"', {dt:date_fld, to_date:to_date});
  if (vid) sp_cond += repl(' AND t1.name LIKE "%%(voucher)s%"', {voucher:vid});
  if (acc) sp_cond += repl(' AND t2.account_head = "%(acc)s"', {acc:acc});

  return repl('SELECT t1.`name`, t1.`%(dt)s`, t1.`customer_name`, t1.net_total, t2.account_head, t2.description, t2.rate, t2.tax_amount \
  	FROM `tab%(parent)s` t1, `tabRV Tax Detail` t2 \
  	WHERE t1.docstatus=1 AND t2.`parenttype` = "%(parent)s" \
  	AND t2.`parent` = t1.`name`  \
  	%(cond)s ORDER BY t1.`name` DESC, t1.%(dt)s DESC', {parent:based_on, cond:sp_cond, dt:date_fld});
}


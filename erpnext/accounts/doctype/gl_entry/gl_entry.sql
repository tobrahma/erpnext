drop trigger if exists before_insert_gle_amount_cb;
delimiter $$
CREATE TRIGGER before_insert_gle_amount_cb BEFORE insert ON `tabGL Entry` FOR EACH ROW
BEGIN
	set NEW.amount := ifnull(NEW.credit,0)-ifnull(NEW.debit,0);
END$$
delimiter ;

drop trigger if exists after_insert_gle_amount_cb;
delimiter $$
CREATE TRIGGER after_insert_gle_amount_cb AFTER insert ON `tabGL Entry` FOR EACH ROW
BEGIN
	declare cb decimal(14,2);

	set @cb := (select closing_balance from `tabGL Entry` where closing_balance is not null and account=new.account and posting_date<=new.posting_date order by posting_date desc limit 1);
	set @cb := ifnull(@cb,0);

	SET @DISABLE_TRIGGERS=1;
	update `tabGL Entry` set closing_balance=(case when name=new.name then @cb+new.amount else closing_balance+new.amount end) where account=new.account and posting_date>=new.posting_date;
	SET @DISABLE_TRIGGERS=NULL;
END$$
delimiter ;


drop trigger before_update_gle_amount_cb;
delimiter $$
CREATE TRIGGER before_update_gle_amount_cb BEFORE update ON `tabGL Entry` FOR EACH ROW
BEGIN
	set NEW.amount := ifnull(NEW.credit,0)-ifnull(NEW.debit,0);
END$$
delimiter ;

drop trigger after_update_gle_amount_cb;
delimiter $$
CREATE TRIGGER after_update_gle_amount_cb AFTER update ON `tabGL Entry` FOR EACH ROW
BEGIN
	declare cb decimal(14,2);

	SET @DISABLE_TRIGGERS=1;

	update `tabGL Entry` set closing_balance=closing_balance-old.amount where account=old.account and posting_date>=old.posting_date;

	set @cb := (select closing_balance from `tabGL Entry` where account=new.account and posting_date<=new.posting_date order by posting_date desc limit 1);
	set @cb = ifnull(@cb,0);

	update `tabGL Entry` set closing_balance=(case when name=new.name then @cb+new.amount else closing_balance+new.amount end) where account=new.account and posting_date>=new.posting_date;

	SET @DISABLE_TRIGGERS=NULL;
END$$
delimiter ;


drop trigger after_delete_gle_amount_cb;
delimiter $$
CREATE TRIGGER after_delete_gle_amount_cb AFTER delete ON `tabGL Entry` FOR EACH ROW
BEGIN
	SET @DISABLE_TRIGGERS=1;
	update `tabGL Entry` set closing_balance=closing_balance-old.amount where account=old.account and posting_date>=old.posting_date;
	SET @DISABLE_TRIGGERS=NULL;
END$$
delimiter ;
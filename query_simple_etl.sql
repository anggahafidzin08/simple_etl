select 
	distinct to2.order_id 
	, to2.order_date 
	, to2.user_id 
	, tp.payment_name 
	, ts.shipper_name
	, to2.order_price 
	, to2.order_discount 
	, tv.voucher_name 
	, tv.voucher_price 
	, to2.order_total 
	, tr.rating_status 
from marketplace.tb_orders to2 
left join marketplace.tb_payments tp 
	using(payment_id)
left join marketplace.tb_shippers ts 
	using(shipper_id)
left join marketplace.tb_vouchers tv 
	using(voucher_id)
left join marketplace.tb_ratings tr 
	using(rating_id)
order by 1
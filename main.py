from classMain import Main

main_obj = Main()
main_obj.records_read()
customer, member, created = main_obj.customer_get_or_create()
membership_price = customer.Value
product = main_obj.product_get()
if member:
    order = main_obj.purchase_product_member(member=member, product=product)
else:
    order = main_obj.purchase_product(customer=customer, product=product)

if created:
    main_obj.print_new_customer_receipt(order, membership_price)
else:
    main_obj.print_existing_customer_receipt(order)

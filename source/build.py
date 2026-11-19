import json
months=[dict(label="Sep 2026",total=72.50,partial=False),dict(label="Oct 2026",total=127.75,partial=False)]
total=sum(m["total"] for m in months); comm_amt=round(total*0.10,2)
comm=[dict(period="September 1 – October 31, 2026",sales=total,comm=comm_amt,status="Pending · paid with the next period"),
      dict(period="November 2026 onward",sales=0,comm=0,status="Next payment after January 31, 2027")]
# units sold Oct 27 - Nov 11 (from refill of Nov 11)
PRODUCTS=[("Diet Coke",14),("Coca-Cola",9),("Coke Zero",5),("Diet Pepsi",3),("Pepsi",2),("Snickers / Mars",2),("Sour Patch Kids",2),("Skittles",1),("Cracker bars",1)]
PRODUCTS=[dict(name=n,qty=q,amt=0) for n,q in PRODUCTS]
work=[
 dict(k="Machine installed",v="Sep 2026",p="Delivered, installed and stocked by Buenavyda, with card, cash and coin payment."),
 dict(k="Logged refill visits",v="3",p="October 7, October 27 and November 11, each one leaving the machine full (207 items)."),
 dict(k="Items in the machine",v="207",p="30 coils: chips, candy and chocolate bars, protein snacks, sodas, energy drinks, Gatorade and protein shakes."),
 dict(k="Drink price",v="$1.00",p="Every drink has been $1.00 since October 27, to give your customers and staff an easy treat while they wait."),
]
inv=[dict(item="A vending machine on site, with card, cash and coin payment, delivered and installed",amt=6500,how="What Buenavyda paid for the machine"),
 dict(item="A full machine of products from day one",amt=255,how="≈207 items at our cost (about half the selling price)")]
invT=round(sum(r["amt"] for r in inv))
D=dict(video="",inv=inv,invTotal=invT,earned=comm_amt,months=months,comm=comm,work=work,avgMonthlyComm=total/2*0.10,visits=[],hpv=0,heat=dict(hours=[],z=[],days=[]),products=PRODUCTS,cats=[])
rep={"__ASOF__":"November 19, 2026","__TOTAL__":f"${total:,.2f}","__COMM__":f"${comm_amt:,.2f}","__INVK__":f"${invT:,.0f}","__VTOT__":f"${invT+comm_amt:,.0f}",
 "__MONTHNOTE__":"Source: Nayax sales records. November is not shown yet because the month is not complete.",
 "__F1__":f"<b>Sales grew from ${months[0]['total']:,.2f} in September to ${months[1]['total']:,.2f} in October</b>, a 76% increase as more customers and staff discovered the machine.",
 "__F2__":"<b>Cold drinks lead: Diet Coke, Coca-Cola and Coke Zero</b> made up most purchases in the last cycle. That is why we keep extra cans ready and moved every drink to $1.00.",
 "__INVNOTE__":"The machine value is what Buenavyda paid for it. Products after the first load are paid from sales, so they are not counted twice. Our time, fuel and restocking are not included in this total.",
 "__DATA__":json.dumps(D)}
html=open("template.html").read()
for k,v in rep.items(): html=html.replace(k,v)
open("index.html","w").write(html)
print(total,comm_amt,invT)

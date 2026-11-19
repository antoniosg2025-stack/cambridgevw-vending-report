import json
months=[dict(label="Sep 2026",total=72.50,partial=False),dict(label="Oct 2026",total=127.75,partial=False)]
total=sum(m["total"] for m in months); comm_amt=round(total*0.10,2)
comm=[dict(period="September 1 – October 31, 2026",sales=total,comm=comm_amt,status="Pending · paid with the next period"),
      dict(period="November 2026 onward",sales=0,comm=0,status="Next payment after January 31, 2027")]
# units sold Oct 27 - Nov 11 (from refill of Nov 11)
PRODUCTS=[("Diet Coke",14),("Coca-Cola",9),("Coke Zero",5),("Diet Pepsi",3),("Pepsi",2),("Snickers / Mars",2),("Sour Patch Kids",2),("Skittles",1),("Cracker bars",1)]
PRODUCTS=[dict(name=n,qty=q,amt=0) for n,q in PRODUCTS]
HPV=6; NV=6; HRS=HPV*NV
labour=round(HRS*25*(1+0.0595+0.0228+0.04)*1.05)
work=[
 dict(k="Machine installed",v="Aug 20",p="August 20, 2026: delivered, installed and stocked by Buenavyda, with card, cash and coin payment."),
 dict(k="Service visits logged",v=f"{NV}",p="Installation and 5 refills, the latest on October 7, October 27 and November 11, each one leaving the machine full."),
 dict(k="Hours per visit",v=f"{HPV} h",p="4 h buying stock and planning the refill, 1 h driving there and back, and 1 h refilling and cleaning on site."),
 dict(k="Items in the machine",v="207",p="30 coils: chips, candy and chocolate bars, protein snacks, sodas, energy drinks, Gatorade and protein shakes."),
 dict(k="Drink price",v="$1.25",p="Every drink is $1.25, to give your customers and staff an easy treat while they wait."),
]
inv=[dict(item="Machine + installation: a vending machine on site, with card, cash and coin payment",amt=7500,how="What Buenavyda paid for the machine ($6,500) and its installation ($1,000)"),
 dict(item="A full machine of products from day one",amt=255,how="≈207 items at our cost (about half the selling price)"),
 dict(item=f"{HRS} hours of service: buying, driving, restocking, cleaning and cash",amt=labour,how="$25/h plus employer CPP 5.95%, EI 2.28%, 4% vacation pay and ≈5% payroll and accounting")]
invT=round(sum(r["amt"] for r in inv))
D=dict(video="",inv=inv,invTotal=invT,earned=comm_amt,months=months,comm=comm,work=work,avgMonthlyComm=total/2*0.10,visits=[],hpv=0,heat=dict(hours=[],z=[],days=[]),products=PRODUCTS,cats=[])
rep={"__ASOF__":"November 19, 2026","__TOTAL__":f"${total:,.2f}","__COMM__":f"${comm_amt:,.2f}","__INVK__":f"${invT:,.0f}","__VTOT__":f"${invT+comm_amt:,.0f}",
 "__MONTHNOTE__":"Source: Nayax sales records. August 20–31 (installation month) and November are not shown because they are not full months.",
 "__F1__":f"<b>Sales grew from ${months[0]['total']:,.2f} in September to ${months[1]['total']:,.2f} in October</b>, a 76% increase as more customers and staff discovered the machine.",
 "__F2__":"<b>Cold drinks lead: Diet Coke, Coca-Cola and Coke Zero</b> made up most purchases in the last cycle. That is why we keep extra cans ready and keep every drink at a friendly $1.25.",
 "__INVNOTE__":"The machine and installation value is what Buenavyda paid for them. Service hours are valued at what the same work would cost the dealership if it hired someone to do it. Products after the first load are paid from sales, so they are not counted twice. Fuel is not included.",
 "__DATA__":json.dumps(D)}
html=open("template.html").read()
for k,v in rep.items(): html=html.replace(k,v)
open("index.html","w").write(html)
print(total,comm_amt,invT)

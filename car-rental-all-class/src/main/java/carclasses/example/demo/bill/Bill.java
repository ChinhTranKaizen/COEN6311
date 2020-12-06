package carclasses.example.demo.bill;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;

// The Bill class is used to generate a bill for the customers
// The bill is based on the chosen car and date of start and end 

//Indicating that it is a JPA entity
@Entity

// Indicate the name of the bill table in DB
@Table(name="Bill")
public class Bill 
{
	//so that JPA recognizes it as the object’s ID
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	// Each bill has it's unique id generated automatically
	// The bill id's column name in DB is billid
	@Column(name="billid")
	private Integer billid;
	
	// The carid is used to identify the car chosen by the customer
	// The car id's column name in DB is carid
	@Column(name="carid")	
	private Integer carid;
	
	// The customerid is used to identify the customer in order to update order history
	// The customer id's column name in DB is customerid
	@Column(name="customerid")
	private Integer customerid;
	
	// The carbill present the amount of payment in dollars
	// The carbill's column name in DB is carbill	
	@Column(name="carbill")
	private Integer carbill;
	
	// The startdate is used to identify the date of starting the rent
	// The startdate's column name in DB is startdate
	@Column(name="startdate")
	private String startdate;
	
	// The enddate is used to identify the date of end of rent
	// The enddate's column name in DB is enddate		
	@Column(name="enddate")
	private String enddate;

	// The cardinfo is used to identify the credit card information of the customer
	// The cardinfo's column name in DB is cardinfo	
	@Column(name="cardinfo")
	private String cardinfo;
	
	// Protected constructor of the bill class
	protected Bill() {
		
	}
	// Public constructor of the bill class	
	public Bill(Integer billid, Integer carid, Integer customerid, Integer carbill, String startdate, String enddate,
			String cardinfo) {
		super();
		this.billid = billid;
		this.carid = carid;
		this.customerid = customerid;
		this.carbill = carbill;
		this.startdate = startdate;
		this.enddate = enddate;
		this.cardinfo = cardinfo;
	}

	// Getters and Setters of the bill class attributes 

	public Integer getBillid() {
		return billid;
	}

	public void setBillid(Integer billid) {
		this.billid = billid;
	}

	public Integer getCarid() {
		return carid;
	}

	public void setCarid(Integer carid) {
		this.carid = carid;
	}

	public Integer getCustomerid() {
		return customerid;
	}

	public void setCustomerid(Integer customerid) {
		this.customerid = customerid;
	}

	public Integer getCarbill() {
		return carbill;
	}

	public void setCarbill(Integer carbill) {
		this.carbill = carbill;
	}

	public String getStartdate() {
		return startdate;
	}

	public void setStartdate(String startdate) {
		this.startdate = startdate;
	}

	public String getEnddate() {
		return enddate;
	}

	public void setEnddate(String enddate) {
		this.enddate = enddate;
	}


	public String getCardinfo() {
		return cardinfo;
	}


	public void setCardinfo(String cardinfo) {
		this.cardinfo = cardinfo;
	}


}

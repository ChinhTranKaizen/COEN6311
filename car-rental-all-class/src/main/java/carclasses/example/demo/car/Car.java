package carclasses.example.demo.car;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;

//indicating that it is a JPA entity
@Entity
@Table(name="Car")
public class Car 
{
	//so that JPA recognizes it as the object’s ID
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	
	@Column(name="carid")
	private Integer carid;
	
	@Column(name="entrydate")
	private String entrydate;
	
	@Column(name="kmdriven")
	private Integer kmdriven;
	
	@Column(name="releaseyear")
	private Integer releaseyear;
	// condition can be: new, slightly used, used, heavily used
	
	@Column(name="condi")
	private String condi;
	
	@Column(name="pricekm")
	private Integer pricekm;
	//if state is true than the car is booked
   
	@Column(name="state")
	private boolean state;
	
    //Brand : e.g. Mercedes, Toyota, etc.
	@Column(name="brand")
    private String brand;
	
    
	//Model: e.g. Corola
	@Column(name="model")
    private String model; 
	
    //style can be: family, sport etc.
	@Column(name="style")
    private String style;
	
	@Column(name="priceday")
    private Integer priceday;
	protected Car() {
		
	}
	
	// Contractor of the car class
	


	

	public Integer getCarid() {
		return carid;
	}


	public Car(Integer carid, String entrydate, Integer kmdriven, Integer releaseyear, String condi, Integer pricekm,
			boolean state, String brand, String model, String style, Integer priceday) {
		super();
		this.carid = carid;
		this.entrydate = entrydate;
		this.kmdriven = kmdriven;
		this.releaseyear = releaseyear;
		this.condi = condi;
		this.pricekm = pricekm;
		this.state = state;
		this.brand = brand;
		this.model = model;
		this.style = style;
		this.priceday = priceday;
	}

	public void setCarid(Integer carid) {
		this.carid = carid;
	}

	public String getEntrydate() {
		return entrydate;
	}

	public void setEntrydate(String entrydate) {
		this.entrydate = entrydate;
	}

	public Integer getKmdriven() {
		return kmdriven;
	}

	public void setKmdriven(Integer kmdriven) {
		this.kmdriven = kmdriven;
	}

	public Integer getReleaseyear() {
		return releaseyear;
	}

	public void setReleaseyear(Integer releaseyear) {
		this.releaseyear = releaseyear;
	}

	
	public String getCondi() {
		return condi;
	}

	public void setCondi(String condi) {
		this.condi = condi;
	}

	public Integer getPricekm() {
		return pricekm;
	}

	public void setPricekm(Integer pricekm) {
		this.pricekm = pricekm;
	}

	public boolean isState() {
		return state;
	}

	public void setState(boolean state) {
		this.state = state;
	}

	public String getBrand() {
		return brand;
	}

	public void setBrand(String brand) {
		this.brand = brand;
	}

	public String getModel() {
		return model;
	}

	public void setModel(String model) {
		this.model = model;
	}

	public String getStyle() {
		return style;
	}

	public void setStyle(String style) {
		this.style = style;
	}

	public Integer getPriceday() {
		return priceday;
	}

	public void setPriceday(Integer priceday) {
		this.priceday = priceday;
	}
	

	
	// getters and setters of the car class attributes

	
}
	

	
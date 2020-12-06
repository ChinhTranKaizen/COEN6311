package carclasses.example.demo.car;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;

//The Car class is used to identify a car 


//indicating that it is a JPA entity
@Entity
//Indicate the name of the car table in DB
@Table(name="Car")
public class Car 
{
	//so that JPA recognizes it as the object’s ID
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)

	// Each car has it's unique id generated automatically
	// The car id's column name in DB is carid
	@Column(name="carid")
	private Integer carid;
	
	// The entry date identifies the date of adding the car to the rental system
	// The entrydate's column name in DB is entrydate
	@Column(name="entrydate")
	private String entrydate;
	
	// The km driven identifies the number of kilometers driven by this car
	// The kmdriven's column name in DB is rkmdriven
	@Column(name="kmdriven")
	private Integer kmdriven;
	
	// The release year identifies the year of manufacturing the car
	// The releaseyear's column name in DB is releaseyear
	@Column(name="releaseyear")
	private Integer releaseyear;
	
	// The condition describes the use state of the car : new, slightly used, used, heavily used
	// The condi's column name in DB is condi
	@Column(name="condi")
	private String condi;
	
	// The price km identifies the price of 1 kilometer driven by the car
	// The pricekm's column name in DB is pricekm
	@Column(name="pricekm")
	private Integer pricekm;

   	// The state identifies the rental state: if state is true than the car is booked
	// The state's column name in DB is state
	@Column(name="state")
	private boolean state;
	
	// The brand identifies the company of manufacturing: e.g. Mercedes, Toyota, etc.
	// The brand's column name in DB is brand
	@Column(name="brand")
    private String brand;
	
    
	// The model identifies the name of car from manufactor:  e.g. Corola
	// The model's column name in DB is model
	@Column(name="model")
    private String model; 
	
	// The style identifies the type of car : family, sport etc.
	// The style's column name in DB is style
	@Column(name="style")
    private String style;
	
	// The price day identifies the price of renting the car for one day
	// The priceday's column name in DB is priceday
	@Column(name="priceday")
    private Integer priceday;
	
	// Protected constructor of the car class
	protected Car() {
		
	}
	
	// Public constructor of the car class	
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

	
	// Getters and Setters of the car class attributes 


	public Integer getCarid() {
		return carid;
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
	

	
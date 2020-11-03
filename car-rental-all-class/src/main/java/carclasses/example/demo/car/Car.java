package carclasses.example.demo.car;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

//indicating that it is a JPA entity
@Entity
public class Car 
{
	//so that JPA recognizes it as the object’s ID
	@Id
	@GeneratedValue(strategy=GenerationType.AUTO)
	private Integer id;
	private String entrydate;
	private Integer kmdriven;
	private Integer releaseyear;
	// condition can be: new, slightly used, used, heavily used
	private String condition;
	private Integer pricekm;
	//if state is true than the car is booked
    private boolean state;
    //Brand : e.g. Mercedes, Toyota, etc.
    private String brand;
    //Model: e.g. Corola
    private String model; 
    //type can be: family, sport etc.
    private String type;
    private Integer priceday;
	protected Car() {
		
	}
	
	// Contractor of the car class
	public Car(Integer id, String entrydate, Integer kmdriven, Integer releaseyear, String condition, Integer pricekm,
			boolean state, String brand, String model, String type, Integer priceday) {
		super();
		this.id = id;
		this.entrydate = entrydate;
		this.kmdriven = kmdriven;
		this.releaseyear = releaseyear;
		this.condition = condition;
		this.pricekm = pricekm;
		this.state = state;
		this.brand = brand;
		this.model = model;
		this.type = type;
		this.priceday = priceday;
	}

	
	// getters and setters of the car class attributes
	public Integer getId() {
		return id;
	}
	public void setId(Integer id) {
		this.id = id;
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
	public String getCondition() {
		return condition;
	}
	public void setCondition(String condition) {
		this.condition = condition;
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
	
	public Integer getPriceday() {
		return priceday;
	}
	public void setPriceday(Integer priceday) {
		this.priceday = priceday;
	}


	public String getModel() {
		return model;
	}


	public void setModel(String model) {
		this.model = model;
	}


	public String getType() {
		return type;
	}


	public void setType(String type) {
		this.type = type;
	}


	
	
}
	

	
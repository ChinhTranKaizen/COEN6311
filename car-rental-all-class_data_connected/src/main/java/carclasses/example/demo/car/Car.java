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
	private String condition;
	private Integer pricekm;
// boolean state (free or not)
	protected Car() {
		
	}

	
	public Car(Integer id, String entrydate, Integer kmdriven, Integer releaseyear, String condition, Integer pricekm) {
		super();
		this.id = id;
		this.entrydate = entrydate;
		this.kmdriven = kmdriven;
		this.releaseyear = releaseyear;
		this.condition = condition;
		this.pricekm = pricekm;
	}


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
	
	
}
	

	
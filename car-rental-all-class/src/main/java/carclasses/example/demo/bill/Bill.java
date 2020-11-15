package carclasses.example.demo.bill;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;


//indicating that it is a JPA entity
@Entity
public class Bill 
{
	//so that JPA recognizes it as the object’s ID
	@Id
	@GeneratedValue(strategy=GenerationType.AUTO)
	private Integer id;
	private Integer IniStaffId;
	private Integer EndStaffId;
	private String carBill;
	private String StartDate;
	private String EndDate;
	
	protected Bill() {
		
	}

	
	
	public Bill(Integer id, Integer iniStaffId, Integer endStaffId, String carBill, String startDate, String endDate) {
		super();
		this.id = id;
		IniStaffId = iniStaffId;
		EndStaffId = endStaffId;
		this.carBill = carBill;
		StartDate = startDate;
		EndDate = endDate;
	}



	public Integer getId() {
		return id;
	}

	public void setId(Integer id) {
		this.id = id;
	}

	public Integer getIniStaffId() {
		return IniStaffId;
	}

	public void setIniStaffId(Integer iniStaffId) {
		IniStaffId = iniStaffId;
	}

	public Integer getEndStaffId() {
		return EndStaffId;
	}

	public void setEndStaffId(Integer endStaffId) {
		EndStaffId = endStaffId;
	}

	
	


	

	public String getCarBill() {
		return carBill;
	}



	public void setCarBill(String carBill) {
		this.carBill = carBill;
	}



	public String getStartDate() {
		return StartDate;
	}

	public void setStartDate(String startDate) {
		StartDate = startDate;
	}

	public String getEndDate() {
		return EndDate;
	}

	public void setEndDate(String endDate) {
		EndDate = endDate;
	}

	
	



}

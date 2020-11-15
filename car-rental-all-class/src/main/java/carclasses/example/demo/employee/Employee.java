package carclasses.example.demo.employee;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;

//indicating that it is a JPA entity
@Entity
@Table(name="Employee")
public class Employee 
{
	//so that JPA recognizes it as the object’s ID
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	
	@Column(name="employeeid")
	private Integer employeeid;
	
	@Column(name="password")
	private String password;
	// position can be : staff, manager, finance
	
	@Column(name="name")
	private String name;
	
	@Column(name="position")
	private String position;
	
	@Column(name="email")
	private String email;
	
	@Column(name="activation")
	private boolean activation;
	protected Employee() {
		
	}
	

	// Contractor of the employee class
	

	public Employee(Integer employeeid, String password, String name, String position, String email,
			boolean activation) {
		super();
		this.employeeid = employeeid;
		this.password = password;
		this.name = name;
		this.position = position;
		this.email = email;
		this.activation = activation;
	}

	// getters and setters of the employee class attributes


	public Integer getEmployeeid() {
		return employeeid;
	}


	public void setEmployeeid(Integer employeeid) {
		this.employeeid = employeeid;
	}


	public String getName() {
		return name;
	}


	public void setName(String name) {
		this.name = name;
	}

	public String getPassword() {
		return password;
	}

	public void setPassword(String password) {
		this.password = password;
	}

	public String getPosition() {
		return position;
	}

	public void setPosition(String position) {
		this.position = position;
	}

	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		this.email = email;
	}


	public boolean isActivation() {
		return activation;
	}


	public void setActivation(boolean activation) {
		this.activation = activation;
	}
	
	
	

}

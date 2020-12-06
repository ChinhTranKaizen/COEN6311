package carclasses.example.demo.employee;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;

//The Employee class is used to identify the employee profile 


//indicating that it is a JPA entity
@Entity

//Indicate the name of the employee table in DB
@Table(name="Employee")
public class Employee 
{
	//so that JPA recognizes it as the object’s ID
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)

	// Each employee has it's unique id generated automatically
	// The employee id's column name in DB is employeeid
	@Column(name="employeeid")
	private Integer employeeid;
	
	// The password of the employee account
	// The password's column name in DB is password
	@Column(name="password")
	private String password;
	
	// The name identifies the name of the employee
	// The name's column name in DB is name
	@Column(name="name")
	private String name;
	
	// The position identifies the position of the employee: : staff, manager, finance
	// The position's column name in DB is position
	@Column(name="position")
	private String position;
	
	// The email identifies the email of the employee
	// The email's column name in DB is email
	@Column(name="email")
	private String email;
	
	// The activation identifies if the employee account is activated or not
	// The activation's column name in DB is activation
	@Column(name="activation")
	private boolean activation;
	
	// Protected constructor of the employee class
	protected Employee() {
		
	}
	
	
	// Public constructor of the employee class	
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

	// Getters and Setters of the employee class attributes 

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

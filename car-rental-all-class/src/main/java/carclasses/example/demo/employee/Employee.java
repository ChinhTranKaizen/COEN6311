package carclasses.example.demo.employee;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

//indicating that it is a JPA entity
@Entity
public class Employee
{
	//so that JPA recognizes it as the object’s ID
	@Id
	@GeneratedValue(strategy=GenerationType.AUTO)
	private Integer id;
	private String name;
	private String password;
	private String position;// May change it enum in next sprint
	private String email;
	private Boolean activation;

	protected Employee() {

	}



	public Employee(Integer id, String name, String password, String position, String email, Boolean activation) {
		super();
		this.id = id;
		this.name = name;
		this.password = password;
		this.position = position;
		this.email = email;
		this.activation = activation;
	}



	public Integer getId() {
		return id;
	}


	public void setId(Integer id) {
		this.id = id;
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

	public String getActivation() {
		return activation;
	}

	public void setActivation(Boolean activation) {
		this.activation = activation;
	}


}

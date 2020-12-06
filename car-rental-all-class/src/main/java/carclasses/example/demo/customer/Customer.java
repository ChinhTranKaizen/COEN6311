package carclasses.example.demo.customer;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;

//The Customer class is used to identify the customer profile 


//indicating that it is a JPA entity
@Entity

//Indicate the name of the customer table in DB
@Table(name="Customer")
public class Customer 
{
	//so that JPA recognizes it as the object’s ID
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)

	// Each customer has it's unique id generated automatically
	// The customer id's column name in DB is customerid
    @Column(name="customerid")
	private Integer customerid;
	
	// The user name identifies the price of the customer's account 
	// The username's column name in DB is username
	@Column(name="username")
	private String username;
	
	// The password of the customer's account 
	// The password's column name in DB is password
	@Column(name="password")
	private String password;
	
	// The first name of the customer
	// The firstname's column name in DB is firstname
	@Column(name="firstname")
	private String firstname;
	
	// The last name of the customer
	// The lastname's column name in DB is lastname
	@Column(name="lastname")
	private String lastname;
	
	// The phone identifies the phone of the customer
	// The phone's column name in DB is phone
	@Column(name="phone")
	private String phone;
	
	// The email identifies the email of the customer
	// The email's column name in DB is email
	@Column(name="email")
	private String email;
	
	// The country identifies the country of residency 
	// The country's column name in DB is country
	@Column(name="country")
	private String country;
	
	// The city identifies the city of residency 
	// The city's column name in DB is city
	@Column(name="city")
	private String city;
	
	// The province identifies the province of residency
	// The province's column name in DB is province
	@Column(name="province")
	private String province;
	
	// The postal identifies the post code of the customer
	// The postal's column name in DB is postal
	@Column(name="postal")
	private String postal;
	
	// The activation identifies if the customer account is activated or not
	// The activation's column name in DB is activation
	@Column(name="activation")
	private boolean activation;
	
	// Protected constructor of the customer class
	protected Customer() {
		
	}

	// Public constructor of the customer class	
	public Customer(Integer customerid, String username, String password, String firstname, String lastname, String phone,
		String email, String country, String city, String province, String postal, boolean activation) {
	super();
	this.customerid = customerid;
	this.username = username;
	this.password = password;
	this.firstname = firstname;
	this.lastname = lastname;
	this.phone = phone;
	this.email = email;
	this.country = country;
	this.city = city;
	this.province = province;
	this.postal = postal;
	this.activation = activation;
}

	// Getters and Setters of the customer class attributes 

	
	public Integer getCustomerid() {
		return customerid;
	}

	public void setCustomerid(Integer customerid) {
		this.customerid = customerid;
	}

	public String getUsername() {
		return username;
	}

	public void setUsername(String username) {
		this.username = username;
	}

	public String getPassword() {
		return password;
	}

	public void setPassword(String password) {
		this.password = password;
	}

	public String getFirstname() {
		return firstname;
	}

	public void setFirstname(String firstname) {
		this.firstname = firstname;
	}

	public String getLastname() {
		return lastname;
	}

	public void setLastname(String lastname) {
		this.lastname = lastname;
	}

	public String getPhone() {
		return phone;
	}

	public void setPhone(String phone) {
		this.phone = phone;
	}

	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	public String getCountry() {
		return country;
	}

	public void setCountry(String country) {
		this.country = country;
	}

	public String getCity() {
		return city;
	}

	public void setCity(String city) {
		this.city = city;
	}

	public String getProvince() {
		return province;
	}

	public void setProvince(String province) {
		this.province = province;
	}

	public String getPostal() {
		return postal;
	}

	public void setPostal(String postal) {
		this.postal = postal;
	}

	public boolean isActivation() {
		return activation;
	}

	public void setActivation(boolean activation) {
		this.activation = activation;
	}
	
	

	// getters and setters of the customer class attributes


	
}	
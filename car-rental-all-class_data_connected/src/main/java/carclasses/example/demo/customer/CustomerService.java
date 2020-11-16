package carclasses.example.demo.customer;



import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;


//the service provide all the methods for the CustomerController class


@Service
public class CustomerService 
{
	@Autowired
	private CustomerRepository customerRepository;
	
	// return all customers in DB		
	public Iterable<Customer> getAllCustomers()
	{
		return customerRepository.findAll();
	}
	//search and  return a customer by id from DB
	public Optional<Customer> getCustomer(Integer customerid)
	{
		return customerRepository.findById(customerid);
	}
	
	// add a customer to DB
	public void addCustomer( Customer customer)
	{
		customerRepository.save(customer);
	}
	// update a customer in DB by its id 
	public void updateCustomer (Integer customerid, Customer customer)
	{
		customerRepository.save(customer);
	}
	// delete a customer from DB by its id 
	public void deleteCustomer( Integer customerid)
	{
		customerRepository.deleteById(customerid);
	}

	
}

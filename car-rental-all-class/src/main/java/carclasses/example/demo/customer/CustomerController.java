package carclasses.example.demo.customer;


import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;
//use REST API to map the HTTP requests
@RestController
public class CustomerController
{
	@Autowired
	private CustomerService customerService;
	
	
	// return all the customers to localhost:3001/customers
	@GetMapping(value="/customers")
	public Iterable<Customer> getAllCustomers()  
	{
		return customerService.getAllCustomers();
	}
	//return a customer using its id to localhost:3001/customer/id
	@GetMapping(value="/customers/{id}")
	public Optional<Customer> getCustomer(@PathVariable Integer id)
	{
		return customerService.getCustomer(id);
	}
	
	// receive a customer from localhost:3001/customers
	@PostMapping(value="/customers")
	public void addCustomer(@RequestBody Customer customer)
	{
		customerService.addCustomer(customer);
	}
	// update a customer using its id to localhost:3001/customer/id
    @PutMapping(value="/customers/{id}")
	public void updateCustomer(@RequestBody Customer customer, @PathVariable Integer id )
	{
    	customerService.updateCustomer(id, customer);
	}
	
  //delete a customer using its id to localhost:3001/customer/id
    @DeleteMapping(value="/customers/{id}")
    public void deleteCustomer(@PathVariable Integer id)
	{
    	customerService.deleteCustomer(id);
	}
	

}

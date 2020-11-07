package carclasses.example.demo.customer;



import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;



@Service
public class CustomerService 
{
	@Autowired
	private CustomerRepository customerRepository;
	
		
	public Iterable<Customer> getAllCustomers()
	{
		return customerRepository.findAll();
	}
	
	public Optional<Customer> getCustomer(Integer id)
	{
		return customerRepository.findById(id);
	}
	

	public void addCustomer( Customer customer)
	{
		customerRepository.save(customer);
	}
	
	public void updateCustomer (Integer id, Customer customer)
	{
		customerRepository.save(customer);
	}
	
	public void deleteCustomer( Integer id)
	{
		customerRepository.deleteById(id);
	}

	
}

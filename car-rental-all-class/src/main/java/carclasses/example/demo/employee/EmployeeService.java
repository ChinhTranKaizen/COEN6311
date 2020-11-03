package carclasses.example.demo.employee;



import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;


//the service provide all the methods for the EmployeeController class


@Service
public class EmployeeService 
{
	@Autowired
	private EmployeeRepository employeeRepository;
	
	// return all employees in DB		
	public Iterable<Employee> getAllEmployees()
	{
		return employeeRepository.findAll();
	}
	//search and  return an employee by id from DB
	public Optional<Employee> getEmployee(Integer id)
	{
		return employeeRepository.findById(id);
	}
	
	// add an employee to DB
	public void addEmployee( Employee employee)
	{
		employeeRepository.save(employee);
	}
	// update an employee in DB by its id 
	public void updateEmployee( Integer id, Employee employee)
	{
		employeeRepository.save(employee);
	}
	// delete an employee from DB by its id 
	public void deleteEmployee( Integer id)
	{
		employeeRepository.deleteById(id);
	}

	
}

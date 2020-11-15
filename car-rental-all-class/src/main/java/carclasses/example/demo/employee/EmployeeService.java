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
<<<<<<< HEAD
	
	// return all employees in DB		
=======


>>>>>>> 5a6b534db9ba507b4933c3eccac7e33d690fad2a
	public Iterable<Employee> getAllEmployees()
	{
		return employeeRepository.findAll();
	}
<<<<<<< HEAD
	//search and  return an employee by id from DB
	public Optional<Employee> getEmployee(Integer employeeid)
=======

	public Optional<Employee> getEmployee(Integer id)
>>>>>>> 5a6b534db9ba507b4933c3eccac7e33d690fad2a
	{
		return employeeRepository.findById(employeeid);
	}
<<<<<<< HEAD
	
	// add an employee to DB
=======


>>>>>>> 5a6b534db9ba507b4933c3eccac7e33d690fad2a
	public void addEmployee( Employee employee)
	{
		employeeRepository.save(employee);
	}
<<<<<<< HEAD
	// update an employee in DB by its id 
	public void updateEmployee( Integer employeeid, Employee employee)
=======

	public void updateEmployee( Integer id, Employee employee)
>>>>>>> 5a6b534db9ba507b4933c3eccac7e33d690fad2a
	{
		  employeeRepository.save(employee);
	}
<<<<<<< HEAD
	// delete an employee from DB by its id 
	public void deleteEmployee( Integer employeeid)
=======

	public void deleteEmployee( Integer id)
>>>>>>> 5a6b534db9ba507b4933c3eccac7e33d690fad2a
	{
		employeeRepository.deleteById(employeeid);
	}


}

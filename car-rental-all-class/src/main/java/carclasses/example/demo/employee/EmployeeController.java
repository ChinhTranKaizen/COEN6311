package carclasses.example.demo.employee;


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
public class EmployeeController
{
	@Autowired
	private EmployeeService employeeService;
	
	
	// return all the employees to localhost:3001/employees
	@GetMapping(value="/employees")
	public Iterable<Employee> getAllEmployees()  
	{
		return employeeService.getAllEmployees();
	}
	//return an employee using its id to localhost:3001/employees/employeeid
	@GetMapping(value="/employees/{employeeid}")
	public Optional<Employee> getEmployee(@PathVariable Integer employeeid)
	{
		return employeeService.getEmployee(employeeid);
	}
	
	// receive an employee from localhost:3001/employees
	@PostMapping(value="/employees")
	public void addEmployee(@RequestBody Employee employee)
	{
		employeeService.addEmployee(employee);
	}
	// update an employee using its id to localhost:3001/employees/employeeid
    @PutMapping(value="/employees/{employeeid}")
	public void updateEmployee(@RequestBody Employee employee, @PathVariable Integer employeeid )
	{
		 employeeService.updateEmployee(employeeid, employee);
	}
	
  //delete an employee using its id to localhost:3001/employees/employeeid
    @DeleteMapping(value="/employees/{employeeid}")
    public void deleteEmployee(@PathVariable Integer employeeid)
	{
		employeeService.deleteEmployee(employeeid);
	}
	

}

package carclasses.example.demo.employee;



import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;



@Service
public class EmployeeService
{
	@Autowired
	private EmployeeRepository employeeRepository;


	public Iterable<Employee> getAllEmployees()
	{
		return employeeRepository.findAll();
	}

	public Optional<Employee> getEmployee(Integer id)
	{
		return employeeRepository.findById(id);
	}


	public void addEmployee( Employee employee)
	{
		employeeRepository.save(employee);
	}

	public void updateEmployee( Integer id, Employee employee)
	{
		employeeRepository.save(employee);
	}

	public void deleteEmployee( Integer id)
	{
		employeeRepository.deleteById(id);
	}


}

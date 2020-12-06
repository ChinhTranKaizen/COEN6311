package carclasses.example.demo.employee;



import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;
//use the Crud Repository methods to manipulate employee repository


@Repository 
public interface EmployeeRepository extends CrudRepository<Employee, Integer>{
	

}

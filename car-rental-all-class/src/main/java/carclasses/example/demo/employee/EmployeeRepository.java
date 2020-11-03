package carclasses.example.demo.employee;


import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
//use the JpaRepository methods to manipulate employee repository
@Repository 
public interface EmployeeRepository extends JpaRepository<Employee, Integer>{
	

}

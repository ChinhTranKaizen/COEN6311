package carclasses.example.demo.customer;


import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
//use the JpaRepository methods to manipulate customer repository
@Repository 
public interface CustomerRepository extends JpaRepository<Customer, Integer>{
	

}

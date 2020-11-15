package carclasses.example.demo.customer;


import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;
//use the JpaRepository methods to manipulate customer repository
@Repository 
public interface CustomerRepository extends CrudRepository<Customer, Integer>{
	

}

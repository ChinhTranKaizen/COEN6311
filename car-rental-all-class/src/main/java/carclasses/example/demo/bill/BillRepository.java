package carclasses.example.demo.bill;


import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

//use the Crud Repository methods to manipulate Bill repository

@Repository 
public interface BillRepository extends CrudRepository<Bill, Integer>{
	

}

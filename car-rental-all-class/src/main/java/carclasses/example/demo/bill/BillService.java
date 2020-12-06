package carclasses.example.demo.bill;



import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

//the service provide all the methods for the BillController class


@Service
public class BillService 
{
	@Autowired
	private BillRepository billRepository;
	
	// return all bills in DB	
		
	public Iterable<Bill> getAllBills()
	{
		return billRepository.findAll();
	}
	
	//search and  return a bill by id from DB

	public Optional<Bill> getBill(Integer billid)
	{
		return billRepository.findById(billid);
	}
	
	// add a bill to DB

	public void addBill( Bill bill)
	{
		billRepository.save(bill);
	}
	
	// update a bill in DB by its id 

	public void updateBill( Integer billid, Bill bill)
	{
		billRepository.save(bill);
	}
	
	// delete a bill from DB by its id 

	public void deleteBill( Integer billid)
	{
		billRepository.deleteById(billid);
	}

	
}

package carclasses.example.demo.bill;


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
public class BillController
{
	@Autowired
	private BillService billService;
	
	
	// return all the bills to localhost:3001/employees
	@GetMapping(value="/bills")
	public Iterable<Bill> getAllBills()  
	{
		return billService.getAllBills();
	}
	
	//return an bill using its id to localhost:3001/bills/billid

	@GetMapping(value="/bills/{billid}")
	public Optional<Bill> getBill(@PathVariable Integer billid)
	{
		return billService.getBill(billid);
	}
	
	// receive an bill from localhost:3001/bills

	@PostMapping(value="/bills")
	public void addBill(@RequestBody Bill bill)
	{
		billService.addBill(bill);
	}
	
	
	// update an bill using its id to localhost:3001/bills/billid
    @PutMapping(value="/bills/{billid}")
	public void updateBill(@RequestBody Bill bill, @PathVariable Integer billid )
	{
    	billService.updateBill(billid, bill);
	}
	
    //delete an bill using its id to localhost:3001/bills/billid

    @DeleteMapping(value="/bills/{billid}")
    public void deleteBill(@PathVariable Integer billid)
	{
    	billService.deleteBill(billid);
	}
	

}

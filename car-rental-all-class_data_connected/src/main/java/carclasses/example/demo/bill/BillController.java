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

@RestController
public class BillController
{
	@Autowired
	private BillService billService;
	
	
	
	@GetMapping(value="/bills")
	public Iterable<Bill> getAllBills()  
	{
		return billService.getAllBills();
	}
	
	@GetMapping(value="/bills/{id}")
	public Optional<Bill> getTBilln(@PathVariable Integer id)
	{
		return billService.getBill(id);
	}
	
	
	@PostMapping(value="/bills")
	public void addBill(@RequestBody Bill bill)
	{
		billService.addBill(bill);
	}
	
    @PutMapping(value="/bills/{id}")
	public void updateBill(@RequestBody Bill bill, @PathVariable Integer id )
	{
    	billService.updateBill(id, bill);
	}
	

    @DeleteMapping(value="/bills/{id}")
    public void deleteBill(@PathVariable Integer id)
	{
    	billService.deleteBill(id);
	}
	

}

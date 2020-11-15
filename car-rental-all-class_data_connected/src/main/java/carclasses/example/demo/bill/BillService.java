package carclasses.example.demo.bill;



import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;



@Service
public class BillService 
{
	@Autowired
	private BillRepository billRepository;
	
		
	public Iterable<Bill> getAllBills()
	{
		return billRepository.findAll();
	}
	
	public Optional<Bill> getBill(Integer id)
	{
		return billRepository.findById(id);
	}
	

	public void addBill( Bill bill)
	{
		billRepository.save(bill);
	}
	
	public void updateBill( Integer id, Bill bill)
	{
		billRepository.save(bill);
	}
	
	public void deleteBill( Integer id)
	{
		billRepository.deleteById(id);
	}

	
}

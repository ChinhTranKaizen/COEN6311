package carclasses.example.demo.report;


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
public class ReportController
{
	@Autowired
	private ReportService reportService;
	
	
	// return all the reports to localhost:3001/reports
	@GetMapping(value="/reports")
	public Iterable<Report> getAllReports()  
	{
		return reportService.getAllReports();
	}
	
	//return an report using its id to localhost:3001/reports/reportid

	@GetMapping(value="/reports/{reportid}")
	public Optional<Report> getReport(@PathVariable Integer reportid)
	{
		return reportService.getReport(reportid);
	}
	
	// receive an report from localhost:3001/reports

	@PostMapping(value="/reports")
	public void addReport(@RequestBody Report report)
	{
		reportService.addReport(report);
	}
	
	
	// update an report using its id to localhost:3001/reports/reportid
    @PutMapping(value="/reports/{reportid}")
	public void updateReport(@RequestBody Report report, @PathVariable Integer reportid )
	{
    	reportService.updateReport(reportid, report);
	}
	
    //delete an report using its id to localhost:3001/reports/reportid

    @DeleteMapping(value="/reports/{reportid}")
    public void deleteReport(@PathVariable Integer reportid)
	{
    	reportService.deleteReport(reportid);
	}
	

}

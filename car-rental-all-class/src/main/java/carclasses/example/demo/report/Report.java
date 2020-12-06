package carclasses.example.demo.report;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;

//The Report class is used to generate a Report of revenue for a certain period 


//indicating that it is a JPA entity
@Entity

//Indicate the name of the bill table in DB
@Table(name="Report")
public class Report 
{
	//so that JPA recognizes it as the object’s ID
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	
	// Each report has it's unique id generated automatically
	// The report id's column name in DB is reportid
	@Column(name="reportid")
	private Integer reportid;
	
	// The report date identifies the date of creation of report
	// The reportdate's column name in DB is reportdate
	@Column(name="reportdate")
	private String reportdate;
	
	// The revenue identifies the income during this particular period
	// The revenue's column name in DB is revenue
	@Column(name="revenue")
	private Integer revenue;
	
	// The duration reported identifies the duration on with the report is based 
	// The durationreported's column name in DB is durationreported
	@Column(name="durationreported")
	private String durationreported;
	
	
	// Protected constructor of the report class	
	protected Report() {
		
	}
	// Public constructor of the report class	
	public Report(Integer reportid, String reportdate, Integer revenue, String durationreported) {
		super();
		this.reportid = reportid;
		this.reportdate = reportdate;
		this.revenue = revenue;
		this.durationreported = durationreported;
	}

	// Getters and Setters of the report class attributes 
	public Integer getReportid() {
		return reportid;
	}

	public void setReportid(Integer reportid) {
		this.reportid = reportid;
	}

	public String getReportdate() {
		return reportdate;
	}

	public void setReportdate(String reportdate) {
		this.reportdate = reportdate;
	}

	public Integer getRevenue() {
		return revenue;
	}

	public void setRevenue(Integer revenue) {
		this.revenue = revenue;
	}

	public String getDurationreported() {
		return durationreported;
	}

	public void setDurationreported(String durationreported) {
		this.durationreported = durationreported;
	}

	

}

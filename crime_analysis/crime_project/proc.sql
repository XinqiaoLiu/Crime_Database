create procedure GetCrimeCount(in Dname varchar(200), out CrimeCount INT)
    begin
      declare v_id int default 1;
      select ID into v_id from crime_app_district_id where Neighborhood = Dname;
      select count(*) into CrimeCount from crime_app_crime where Area_id = v_id;
    end//

create procedure GetDanger(in g varchar(200), in a varchar(200),in Dname varchar(200),in st datetime, in et datetime, out r float)
    begin
      declare v_id int default 1;
      declare crimecount int default 1;
      declare dangersum float default 1.0;
      select ID into v_id from crime_app_district_id where Neighborhood = Dname;
      select count(*) into crimecount from crime_app_crime where Area_id = v_id and Ctime>st and Ctime<et;

      select sum(Level) into dangersum from
        ((select Type from crime_app_crime where Area_id = v_id and Ctime>st and Ctime<et) A
        join
        (select Type,Level from crime_app_danger where Gender=g and Age=a) B
        on A.Type = B.Type);

      set r = dangersum/crimecount;

    end//

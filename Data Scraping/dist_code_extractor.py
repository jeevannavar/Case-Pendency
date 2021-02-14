string = '<option value="1" >Malda</option><option value="2" >Hooghly</option><option value="3" >Calcutta</option><option value="4" >Jalpaiguri</option><option value="6" >Coochbehar</option><option value="7" >Paschim Medinpur</option><option value="8" >Birbhum</option><option value="9" >Purba Medinipur</option><option value="10" >Purulia</option><option value="11" >Howrah</option><option value="12" >Murshidabad</option><option value="13" >South Dinajpur</option><option value="14" >North  Twenty Four Parganas</option><option value="17" >Darjeeling</option><option value="18" >Purba Bardhaman</option><option value="19" >Bankura</option><option value="20" >South Twenty Four Parganas</option><option value="21" >North Dinajpur</option><option value="22" >Nadia</option><option value="23" >kalimpong</option><option value="24" >Paschim Bardhaman</option><option value="25" >Jhargram</option>                      </select>'
separated = string.split("</option>")
codes = [each[15:].split('" >') for each in separated[:-1]]
print(codes)

#districts = [each[1] for each in codes]
#codes = [each[0] for each in codes]
codes = [",".join([each[1],each[0]]) for each in codes]
print(len(codes))
print("\n".join(sorted(codes)))
#print("\n".join(districts))


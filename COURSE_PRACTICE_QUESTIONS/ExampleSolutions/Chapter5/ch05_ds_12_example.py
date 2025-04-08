# Chapter 5: Data Structures

# Sets for practice problems 1-4
amino_acids_set1 = {'glycine', 'alanine', 'valine', 'serine', 'leucine', 'phenylalanine'}
amino_acids_set2 = {'proline', 'glutamine', 'asparagine', 'valine', 'histidine', 'phenylalanine'}

#* 1. Union of Two Sets
union_set = amino_acids_set1.union(amino_acids_set2)
print(union_set)


#* 2. Intersection of Two Sets
intersection_set = amino_acids_set1.intersection(amino_acids_set2)
print(intersection_set)


#* 3. Difference Between Two Sets
difference_set = amino_acids_set1.difference(amino_acids_set2)
print(difference_set)


#* 4. Symmetric Difference of Two Sets
symmetric_difference_set = amino_acids_set1.symmetric_difference(amino_acids_set2)
print(symmetric_difference_set)


#* 5. Disjoint Sets Check
amino_acids_set3 = {'glycine', 'serine', 'glutamine'}
amino_acids_set4 = {'proline', 'histidine', 'asparagine'}
are_disjoint = amino_acids_set3.isdisjoint(amino_acids_set4)
print(are_disjoint)


#* 6. Superset and Subset Check
amino_acids_set5 = {'glycine', 'valine', 'serine', 'phenylalanine', 'glutamine'}
amino_acids_set6 = {'valine', 'serine'}
is_superset = amino_acids_set5.issuperset(amino_acids_set6)
is_subset = amino_acids_set6.issubset(amino_acids_set5)
print(is_superset, is_subset)


#* 7. Handling Missing Elements
amino_acids_set7 = {'glycine', 'valine', 'serine', 'phenylalanine'}
amino_acids_set8 = {'serine', 'glutamine', 'valine', 'proline'}
missing_elements = amino_acids_set7.difference(amino_acids_set8)
print(missing_elements)

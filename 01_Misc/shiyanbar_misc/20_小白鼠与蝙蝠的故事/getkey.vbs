Dim num(5,5)
num(0,0) = 70
num(0,1) = 33
num(0,2) = 108
num(0,3) = 545
num(0,4) = 78
num(1,0) = 121
num(1,1) = 87
num(1,2) = 11
num(1,3) = 465
num(1,4) = 575
num(2,0) = 105
num(2,1) = 33
num(2,2) = 45
num(2,3) = 356
num(2,4) = 251
num(3,0) = 116
num(3,1) = 104
num(3,2) = 333
num(3,3) = 356
num(3,4) = 457
num(4,0) = 85
num(4,1) = 33
num(4,2) = 33
num(4,3) = 24
num(4,4) = 564
For i = 0 To 4 Step 1
    For j = 0 To 4 Step 1
        If (j = 0 Or i + j = 2) Then
            this_is_key = this_is_key & Chr(num(i, j))
        Else If (j = 0 Or i = 2 + j) Then
            this_is_key = this_is_key & Chr(num(i, j))
        End If
    End If
Next
Next
MsgBox this_is_key
